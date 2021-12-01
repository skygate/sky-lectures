import Navigation from "./Navigation";
import Footer from "./Footer";
import Logo from "./Logo";

import "./Sidebar.modules.scss";

function Sidebar() {
  return (
    <nav className="sidebar">
      <Logo />
      <Navigation />
      <Footer />
    </nav>
  );
}

export default Sidebar;
