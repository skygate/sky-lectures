import { useRef, useCallback, useState, useEffect } from "react";

import styles from "./Presentation.module.scss";

interface Props {
  item: Item;
  height: number;
}

interface Item {
  id: string;
  author: string;
  title: string;
  startTime: Date;
  endTime: Date;
}

function calculateTop(height: number, startTime: Date) {
  const startHour = startTime.getHours();
  const startMinute = startTime.getMinutes();

  let minutesHeight = 0;
  const oneHourHeight = height / 13;

  if (startMinute > 0) {
    minutesHeight = (oneHourHeight / 60) * startMinute;
  }

  const top = (startHour - 8) * oneHourHeight + minutesHeight;

  return top;
}

function calculateBottom(height: number, date: Date) {
  const hours = date.getHours();
  const minutes = date.getMinutes();

  let minutesHeight = 0;
  const oneHourHeight = height / 13;

  if (minutes > 0) {
    minutesHeight = (oneHourHeight / 60) * minutes;
  }

  const bottom = (hours - 8) * oneHourHeight + minutesHeight;

  return bottom;
}

function Presentation({ item, height }: Props) {
  const [anchorPoint, setAnchorPoint] = useState({ x: 0, y: 0 });
  const [showMenu, setShowMenu] = useState(false);
  const presentationDiv = useRef<HTMLHeadingElement>(null);
  const top = calculateTop(height, item.startTime);
  const bottom = calculateBottom(height, item.endTime);

  const handleClick = useCallback(
    () => (showMenu ? setShowMenu(false) : null),
    [showMenu]
  );

  console.log(anchorPoint);

  const handleContextMenu = useCallback(
    (event) => {
      event.preventDefault();
      setAnchorPoint({ x: event.pageX, y: event.pageY });
      setShowMenu(true);
      console.log("HELLO");
    },
    [setShowMenu]
  );

  useEffect(() => {
    const div = presentationDiv.current;

    if (div) {
      document.addEventListener("click", handleClick);
      div.addEventListener("contextmenu", handleContextMenu);

      return () => {
        document.removeEventListener("click", handleClick);
        div.removeEventListener("contextmenu", handleContextMenu);
      };
    }
  });

  return (
    <div
      className={styles.presentationContainer}
      style={{ top: top, height: bottom - top }}
      ref={presentationDiv}
    >
      <div
        className={`${styles.presentation} ${bottom - top < 20 && styles.hide}`}
      >
        <p>{item.title}</p>
        <p>{item.author}</p>
      </div>
      {!showMenu && (
        <div
          className={`${styles.hoverBlock} ${bottom - top > 20 && styles.hide}`}
          style={{ top: bottom - top + 5, right: 0 }}
        >
          <p>{item.title}</p>
          <p>{item.author}</p>
        </div>
      )}
      {showMenu ? (
        <div className={styles.menu}>
          <button className={styles.button}>Edit</button>
          <button className={styles.button}>Delete</button>
        </div>
      ) : (
        <> </>
      )}
    </div>
  );
}

export default Presentation;
