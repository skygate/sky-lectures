import styles from "./FilterButton.module.scss";

interface Props {
  children: string;
  value: number;
  currentValue: number;
  handleClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
}

function FilterButton({
  children,
  value = 0,
  currentValue,
  handleClick,
}: Props) {
  return (
    <button
      type="button"
      className={`${styles.filterButton} ${
        currentValue === value && styles["active"]
      }`}
      onClick={handleClick}
      value={value}
    >
      {children}
    </button>
  );
}
export default FilterButton;
