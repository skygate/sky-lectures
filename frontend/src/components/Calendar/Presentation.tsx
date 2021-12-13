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
  const top = calculateTop(height, item.startTime);
  const bottom = calculateBottom(height, item.endTime);

  return (
    <div
      className={styles.presentation}
      style={{ top: top, height: bottom - top }}
    >
      <p>{item.author}</p>
      <p>{item.title}</p>
    </div>
  );
}

export default Presentation;
