import React from "react";
import CustomButton from "./CustomButton";

import styles from "./Filter.module.scss";

interface Props {
  selectTypeHandler: (e: React.MouseEvent<HTMLButtonElement>) => void;
  selectCategoryHandler: (e: React.MouseEvent<HTMLButtonElement>) => void;
  showFilter: boolean;
  type: string;
  category: string;
}

function Filter({
  selectTypeHandler,
  selectCategoryHandler,
  showFilter,
  type,
  category,
}: Props) {
  return (
    <div className={`${styles["filter"]} ${showFilter && styles["active"]}`}>
      <div className={styles["filter__type"]}>
        <p className={styles["filter__type--header"]}>Type:</p>
        <div className={styles["filter__type--group"]}>
          <div className={styles["filter__type--button"]}>
            <CustomButton
              handleClick={selectTypeHandler}
              value="presentation"
              filter={type}
            >
              Presentation
            </CustomButton>
          </div>
          <div className={styles["filter__type--button"]}>
            <CustomButton
              handleClick={selectTypeHandler}
              value="video"
              filter={type}
            >
              Video
            </CustomButton>
          </div>
        </div>
      </div>
      <div className={styles["filter__category"]}>
        <p className={styles["filter__category--header"]}>Category:</p>
        <div className={styles["filter__category--group"]}>
          <div className={styles["filter__category--button"]}>
            <CustomButton
              handleClick={selectCategoryHandler}
              value="back-end"
              filter={category}
            >
              Back-End
            </CustomButton>
          </div>
          <div className={styles["filter__category--button"]}>
            <CustomButton
              handleClick={selectCategoryHandler}
              value="front-end"
              filter={category}
            >
              Front-End
            </CustomButton>
          </div>
        </div>
        <div className={styles["filter__category--group"]}>
          <div className={styles["filter__category--button"]}>
            <CustomButton
              handleClick={selectCategoryHandler}
              value="design"
              filter={category}
            >
              Design
            </CustomButton>
          </div>
          <div className={styles["filter__category--button"]}>
            <CustomButton
              handleClick={selectCategoryHandler}
              value="trending"
              filter={category}
            >
              Trednding
            </CustomButton>
          </div>
        </div>
        <div className={styles["filter__category--group"]}>
          <div className={styles["filter__category--button"]}>
            <CustomButton
              handleClick={selectCategoryHandler}
              value="ml"
              filter={category}
            >
              ML
            </CustomButton>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Filter;
