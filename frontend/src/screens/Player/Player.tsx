import Sidebar from "../../components/Sidebar/Sidebar";
import styles from "./Player.module.scss";
import { ReactComponent as PersonIcon } from "../../assets/icons/person.svg";
import { ReactComponent as HeartIcon } from "../../assets/icons/heart.svg";
import { ReactComponent as ClockIcon } from "../../assets/icons/clock.svg";
import { ReactComponent as ShareIcon } from "../../assets/icons/share.svg";
import NewComment from "../../components/NewComment/NewComment";
import { useState } from "react";
const Player = () => {
  const [visible, setVisibility] = useState(false);
  function showMore(): void {
    setVisibility(!visible);
  }
  return (
    <>
      <Sidebar />
      <div className={styles["player-content"]}>
        <div className={styles["video-player"]}></div>
        <div className={styles["video-info"]}>
          <div className={styles["video-name"]}>
            Presentation's name
            <div className={styles["video-actions"]}>
              <HeartIcon />
              <ClockIcon />
              <ShareIcon />
            </div>
          </div>
          <div className={styles["author"]}>
            <PersonIcon />
            <div className={styles["author-info"]}>
              <div className={styles["author-name"]}>Janek</div>
              <div className={styles["author-works"]}>5 works</div>
            </div>
          </div>
          <div className={styles["video-description"]}>
            <div
              className={
                visible
                  ? styles["video-description-more"]
                  : styles["video-description-less"]
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
          <a onClick={showMore} className={styles["show-more-btn"]}>
            {visible ? "hide" : "show more"}
          </a>
        </div>
        <div className={styles["comments-section"]}>
          <p>Comments</p>
          <NewComment />
        </div>
      </div>
    </>
  );
};
export default Player;
