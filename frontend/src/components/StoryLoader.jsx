import {useState, useEffect} from 'react';
import {useParams, useNavigate} from "react-router-dom";
import axios from 'axios';
import LoadingStatus from './LoadingStatus.jsx';
import StoryGame from "./StoryGame.jsx";
import {API_BASE_URL} from "../utils.js";

function StoryLoader(){
    const {id} = useParams();
    const navigate = useNavigate();
    const [story,setStory] = useState(null);
    const [loading,setloading] = useState(true);
    const [error,setError] = useState(null);

    useEffect(() => {
        loadStory(id)
    },[id])

    const loadStory = async(storyId) => {
        setloading(true)
        setError(null)

        try{
            const response = await axios.get(`${API_BASE_URL}/stories/${storyId}/complete`)
            setStory(response.data)
            setloading(false)
        }catch(err){
            if(err.response?.status === 404){
                setError("Story is Not found")
            }else{
            setError("Failed to load story")}
        }finally{setloading(false)}
    }

    const createNewStory = () => {
        navigate("/")
    }

    if(loading){
        return <LoadingStatus theme={"story"}/>

    }

    if(error){
        return <div className="story-loader">
            <div className="error-message">
                <h2>Story Not Found</h2>
                <p>{error}</p>
                <button onCLick={createNewStory}>Go to Story Generator</button>
            </div>
        </div>
    }

    if(story){
        return <div className="story-loader">
            <StoryGame story={story} on NewStory={createNewStory}/>
        </div>
    }


}

export default StoryLoader;
