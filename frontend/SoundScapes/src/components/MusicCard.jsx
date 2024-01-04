import Backward from "./backward";
import Forward from "./forward";
import Pause from "./pause";
import Play from "./play";

export default function MusicCard(props){
    return <div className="card border-0">
        <img src={props.aks} alt="" className="card-img-top" />
        <div class="card-body">
             <h2 class="card-title">{props.name}</h2>
             <h5 class="card-text">{props.singer}</h5>
        </div>
        <div className="d-inline-flex justify-content-center">
            <Backward />
            <Play />
            <Forward />
        </div>

        
    </div>
}