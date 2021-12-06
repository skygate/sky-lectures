import Sidebar from "../../components/Sidebar/Sidebar";
import "./Player.modules.scss";
import person from "../../assets/icons/person.svg";
import heart from "../../assets/icons/heart.svg";
import clock from "../../assets/icons/clock.svg";
import share from "../../assets/icons/share.svg";
import Comments from "../../components/comments/comments";
import { useState } from "react";
const Player = () => {
  const [visible, setVisibility] = useState(false);
  function showMore(): void {
    setVisibility(!visible);
  }
  return (
    <>
      <Sidebar />
      <div className="player-content">
        <div className="video-player">s</div>
        <div className="video-info">
          <div className="video-name">
            Presentation's name
            <div className="video-actions">
              <img src={heart} alt="heart" />
              <img src={clock} alt="clock" />
              <img src={share} alt="share" />
            </div>
          </div>
          <div className="author">
            <img src={person} alt="person" />
            <div className="author-info">
              <div className="author-name">Janek</div>
              <div className="author-works">5 works</div>
            </div>
          </div>
          <div className="video-description">
            <div
              className={
                visible ? "video-description-more" : "video-description-less"
              }
            >
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit
              nesciunt dolore animi illo similique! Minus dolorum ea nihil quasi
              quis pariatur veritatis, exercitationem magnam aperiam dignissimos
              molestiae reprehenderit eveniet quas culpa rem modi vel molestias.
              Voluptatum rem autem mollitia. Dolorem necessitatibus aperiam unde
              in, suscipit saepe nesciunt accusamus eligendi fugiat enim
              quaerat. Animi commodi, porro natus laudantium voluptatibus
              cupiditate fugiat, laborum consectetur temporibus alias eligendi
              perferendis nobis ducimus modi vitae nemo voluptates facilis
              minima. Enim sed porro voluptate optio voluptatibus! Facilis
              cupiditate voluptates temporibus maxime id quasi ex quia ipsa cum
              nisi rerum voluptatem et deserunt assumenda possimus consequuntur,
              eveniet commodi odit maiores perferendis pariatur. Ad consectetur
              delectus commodi beatae ex in, hic eius. Autem obcaecati fugiat
              itaque rerum provident aliquam consequatur numquam eligendi alias
              hic, soluta odio ab id tenetur? Rem nostrum necessitatibus laborum
              sint ratione aliquid iusto distinctio repellat porro maxime
              laboriosam, sit pariatur amet vel culpa quo, debitis sapiente
              minima quam velit repudiandae cumque ab aspernatur iste. Nam
              delectus vel incidunt odit enim asperiores fugit pariatur dolore,
              ipsum unde, error eaque temporibus consequatur, quasi quam
              laboriosam eius deleniti voluptas minus. Consequuntur, eveniet
              illum esse nisi nulla minima rem adipisci harum! In beatae
              doloribus natus eligendi ratione deleniti.
            </div>
          </div>
          <a onClick={showMore} className="show-more-btn">
            {visible ? "hide" : "show more"}
          </a>
        </div>
        <div className="comments-section">
          <p>Comments</p>
          <Comments />
        </div>
      </div>
    </>
  );
};
export default Player;
