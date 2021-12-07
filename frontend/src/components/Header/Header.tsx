import {  ReactNode } from "react";
import "./Header.modules.scss";

function Header({ children }: { children: ReactNode }) {
  return <header className="header">{children}</header>;
}

export default Header;
