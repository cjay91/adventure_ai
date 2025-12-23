import { useState } from "react";

function ThemeInput({onSubmit}) {
    const [theme, setTheme] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!theme.trim()){
            setError("Theme cannot be empty.");
            return;
        }

        onSubmit(theme);
    }

    return <div className="theme-input-container">
        <h2>Generate your Adventure</h2>
        <p>Enter a theme for your interactive story</p>

        <form onSubmit={handleSubmit}>
            <div className="input-group">
                <input
                    type="text"
                    value={theme}
                    onChange={(e) => setTheme(e.target.value)}
                    placeHolder= "Enter a theme(E.g Pirates, Space Exploration)"
                    className= {error ? "error": ""}
                />
                {error && <p className="error-text">{error}</p>}    
            </div> 
            <button type="submit" className='generate-button'>
                Generate Story
            </button>
        </form>
        </div>
}

export default ThemeInput;