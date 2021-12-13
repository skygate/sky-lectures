import { useState, useRef, useEffect } from "react";
import { compareAsc } from "date-fns";

import Presentation from "./Presentation";

import styles from "./Day.module.scss";

interface Props {
  presentations: PresentationData[];
  date: Date;
}

interface PresentationData {
  id: string;
  author: string;
  title: string;
  startTime: Date;
  endTime: Date;
}

function Day({ presentations, date }: Props) {
  const [height, setHight] = useState(0);
  const divRef = useRef<HTMLDivElement>(null);

  const filteredPresentations = presentations.filter(
    (item) =>
      compareAsc(
        new Date(item.startTime).setHours(0, 0, 0, 0),
        date.setHours(0, 0, 0, 0)
      ) === 0
  );

  const items = [];

  for (let i = 8; i < 21; i++) {
    items.push(<div key={i} className={styles.hour}></div>);
  }

  useEffect(() => {
    if (divRef.current) {
      setHight(divRef.current.clientHeight);
    }
  }, [divRef]);

  return (
    <div className={styles.day} ref={divRef}>
      {items}

      {filteredPresentations.map((item, i) => (
        <Presentation key={i} item={item} height={height} />
      ))}
    </div>
  );
}

export default Day;
