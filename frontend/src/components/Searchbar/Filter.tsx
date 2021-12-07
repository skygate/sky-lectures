import React from "react";
import CustomButton from "./CustomButton";

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
    <div className={`searchbar__filter--container ${showFilter && "active"} `}>
      <div className="searchbar__filterType">
        <p className="searchbar__filterType--header">Type:</p>
        <div className="searchbar__filterType--group">
          <div className="searchbar__filterType--button">
            <CustomButton
              handleClick={selectTypeHandler}
              value="presentation"
              filter={type}
            >
              Presentation
            </CustomButton>
          </div>
          <div className="searchbar__filterType--button">
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
      <div className="searchbar__filterCategory">
        <p className="searchbar__filterCategory--header">Category:</p>
        <div className="searchbar__filterCategory--group">
          <div className="searchbar__filterCategory--button">
            <CustomButton
              handleClick={selectCategoryHandler}
              value="back-end"
              filter={category}
            >
              Back-End
            </CustomButton>
          </div>
          <div className="searchbar__filterCategory--button">
            <CustomButton
              handleClick={selectCategoryHandler}
              value="front-end"
              filter={category}
            >
              Front-End
            </CustomButton>
          </div>
        </div>
        <div className="searchbar__filterCategory--group">
          <div className="searchbar__filterCategory--button">
            <CustomButton
              handleClick={selectCategoryHandler}
              value="design"
              filter={category}
            >
              Design
            </CustomButton>
          </div>
          <div className="searchbar__filterCategory--button">
            <CustomButton
              handleClick={selectCategoryHandler}
              value="trending"
              filter={category}
            >
              Trednding
            </CustomButton>
          </div>
        </div>
        <div className="searchbar__filterCategory--group">
          <div className="searchbar__filterCategory--button">
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
