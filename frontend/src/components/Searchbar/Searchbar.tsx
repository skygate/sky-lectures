import React, { useState } from "react";
import { ReactComponent as SearchIcon } from "../../assets/icons/search.svg";
import { ReactComponent as FilterIcon } from "../../assets/icons/filter.svg";

import SearchBarModal from "../Modal/SearchBarModal";
import SearchBarModalContent from "./SearchBarModalContent";
import CustomButton from "./CustomButton";
import "./Searchbar.modules.scss";

const presentationList = [
  "react presentation",
  "JS presentation",
  "SASS presentation",
  "Design presentation",
];

function Searchbar() {
  const [showFilter, setShowFilter] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [searchValue, setSearchValue] = useState("");
  const [type, setType] = useState("presentation");
  const [category, setCategory] = useState("back-end");
  const [searchList, setSearchList] = useState<string[]>([]);

  function handleChange(e: React.FormEvent<HTMLInputElement>) {
    setShowFilter(false);
    setSearchValue(e.currentTarget.value);
    setShowModal(true);
    setSearchList(
      presentationList.filter((item) =>
        item.toLocaleLowerCase().includes(searchValue.toLowerCase())
      )
    );
  }

  function toggleFilter() {
    if (!showFilter) {
      setShowModal(true);
    } else {
      setShowModal(false);
    }
    setShowFilter((state) => !state);
    setSearchList([]);
    setSearchValue("");
  }

  function selectTypeHandler(e: React.MouseEvent<HTMLButtonElement>) {
    setType(e.currentTarget.value);
  }

  function selectCategoryHandler(e: React.MouseEvent<HTMLButtonElement>) {
    setCategory(e.currentTarget.value);
  }

  function modalHandler() {
    setShowFilter(false);
    setSearchList([]);
    setSearchValue("");
    setShowModal(false);
  }

  function clickCaptureHandler() {
    setShowModal(true);
    setShowFilter(false);
    setSearchList([]);
    setSearchValue("");
  }

  return (
    <div className="searchbar">
      <div className="searchbar__form">
        <input
          type="search"
          name="search"
          className="searchbar__form--input"
          placeholder="Search"
          value={searchValue}
          onChange={handleChange}
          onClickCapture={clickCaptureHandler}
        />
        {searchList.length > 0 && searchValue && (
          <div className="searchbar__form--searchList">
            {searchList.slice(0, 5).map((item, index) => (
              <div className="searchbar__form--searchItem" key={index}>
                {item}
              </div>
            ))}
          </div>
        )}
        <div className="searchbar__container">
          <button
            className="searchbar__container--btn filter"
            onClick={toggleFilter}
          >
            <FilterIcon />
          </button>
          <button className="searchbar__container--btn search">
            <SearchIcon />
          </button>
        </div>
        <div
          className={`searchbar__filter--container ${showFilter && "active"} `}
        >
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
      </div>
      <SearchBarModal modalOpen={showModal}>
        <SearchBarModalContent clickHandler={modalHandler} />
      </SearchBarModal>
    </div>
  );
}

export default Searchbar;
