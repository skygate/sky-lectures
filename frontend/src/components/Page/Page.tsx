import React from "react";

import Sidebar from "../Sidebar/Sidebar";
import Searchbar from "../Searchbar/Searchbar";
import Header from "../Header/Header";
import UserDetails from "../UserDetails/UserDetails";

import styles from "./Page.module.scss";

interface Props {
  children: React.ReactNode;
  showSearchbar?: boolean;
  textHeader?: string;
}

function Page({ children, showSearchbar = true, textHeader }: Props) {
  return (
    <div className={styles.page}>
      <Sidebar />
      <div className={styles.wrapper}>
        <Header>
          {showSearchbar ? (
            <Searchbar />
          ) : (
            <span className={styles.textHeader}>{textHeader}</span>
          )}
          <UserDetails />
        </Header>
        <div className={styles.container}>{children}</div>
      </div>
    </div>
  );
}

export default Page;
