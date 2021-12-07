import React, { useState } from "react";
import { ReactComponent as SearchIcon } from "../../assets/icons/search.svg";
import { ReactComponent as FilterIcon } from "../../assets/icons/filter.svg";

import SearchBarModal from "../Modal/SearchBarModal";
import SearchBarModalContent from "./SearchBarModalContent";
import Filter from "./Filter";

import "./Searchbar.modules.scss";

const presentationList = [
  "react presentation",
  "JS presentation",
  "SASS presentation",
  "Design presentation",
];

function Searchbar() {
  const [searchValue, setSearchValue] = useState("");
  const [type, setType] = useState("presentation");
  const [category, setCategory] = useState("back-end");
  const [searchList, setSearchList] = useState<string[]>([]);
  const [searchbarState, setSearchbarState] = useState({
    showFilter: false,
    showModal: false,
  });

  function handleChange(e: React.FormEvent<HTMLInputElement>) {
    setSearchbarState({
      showFilter: false,
      showModal: true,
    });
    setSearchValue(e.currentTarget.value);
    setSearchList(
      presentationList.filter((item) =>
        item.toLocaleLowerCase().includes(searchValue.toLowerCase())
      )
    );
  }

  function toggleFilter() {
    if (!searchbarState.showFilter) {
      setSearchbarState((prevState) => ({
        showFilter: !prevState.showFilter,
        showModal: true,
      }));
    } else {
      setSearchbarState((prevState) => ({
        showFilter: !prevState.showFilter,
        showModal: false,
      }));
    }
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
    setSearchbarState({
      showFilter: false,
      showModal: false,
    });
    setSearchList([]);
    setSearchValue("");
  }

  function clickCaptureHandler() {
    setSearchbarState({
      showFilter: false,
      showModal: true,
    });
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
          autoComplete="off"
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
        <Filter
          selectTypeHandler={selectTypeHandler}
          selectCategoryHandler={selectCategoryHandler}
          showFilter={searchbarState.showFilter}
          type={type}
          category={category}
        />
      </div>
      <SearchBarModal modalOpen={searchbarState.showModal}>
        <SearchBarModalContent clickHandler={modalHandler} />
      </SearchBarModal>
    </div>
  );
}

export default Searchbar;
