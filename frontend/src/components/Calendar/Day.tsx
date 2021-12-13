import { useState, useRef, useEffect } from "react";

import styles from "./Day.module.scss";

import Presentation from "./Presentation";

// interface Props {
//   author: string;
//   title: string;
//   startDate: string;
//   endDate: string;
// }

const presentation = [
  {
    id: "01",
    author: "Author",
    title: "presentation name",
    startTime: new Date("2021-12-10T10:40:00"),
    endTime: new Date("2021-12-10T11:40:00"),
  },
  {
    id: "02",
    author: "Author",
    title: "presentation name",
    startTime: new Date("2021-12-10T16:40:00"),
    endTime: new Date("2021-12-10T19:40:00"),
  },
  // {
  //   id: "03",
  //   author: "Author",
  //   title: "presentation name",
  //   startTime: "15:30",
  //   endTime: "16:30",
  // },
];

function Day() {
  const [height, setHight] = useState(0);
  const divRef = useRef<HTMLDivElement>(null);

  const items = [];

  useEffect(() => {
    if (divRef.current) {
      setHight(divRef.current.clientHeight);
    }
  }, [divRef]);

  for (let i = 8; i < 21; i++) {
    items.push(<div key={i} className={styles.hour}></div>);
  }
  return (
    <div className={styles.day} ref={divRef}>
      {items}

      {presentation.map((item, i) => (
        <Presentation key={i} item={item} height={height} />
      ))}
    </div>
  );
}

export default Day;
