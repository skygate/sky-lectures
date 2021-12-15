import styles from "./CustomButton.module.scss";

interface Props {
  children: string;
  handleClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
  type?: "button" | "submit" | "reset";
  reverseColor?: boolean;
}

function CustomButton({
  children,
  handleClick,
  type = "button",
  reverseColor = false,
}: Props) {
  return (
    <button
      type={type}
      className={`${styles.customButton} ${
        reverseColor && styles.reverseColor
      } `}
      onClick={handleClick}
    >
      {children}
    </button>
  );
}
export default CustomButton;
