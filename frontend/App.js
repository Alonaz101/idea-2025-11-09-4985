// frontend/App.js
import React, { useState } from 'react';

function App() {
  const [mood, setMood] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const submitMood = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('/api/mood', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: 1, mood_name: mood })
      });
      if (!response.ok) throw new Error('Failed to fetch recipes');
      const data = await response.json();
      setRecipes(data.recipes);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Mood to Recipe Matcher</h1>
      <input value={mood} onChange={e => setMood(e.target.value)} placeholder="Enter your mood" />
      <button onClick={submitMood} disabled={loading}>Get Recipes</button>
      {error && <div style={{color: 'red'}}>{error}</div>}
      <ul>
        {recipes.map(recipe => (
          <li key={recipe.id}>{recipe.name} - {recipe.cook_time_minutes} min</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
