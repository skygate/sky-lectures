import Navigation from "./Navigation";
import Logout from "./Logout";
import Logo from "./Logo";

import "./Sidebar.modules.scss";

function Sidebar() {
  return (
    <nav className="sidebar">
      <Logo />
      <Navigation />
      <Logout />
    </nav>
  );
}

export default Sidebar;
