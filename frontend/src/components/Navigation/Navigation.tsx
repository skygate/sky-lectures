import "./Navigation.modules.scss";
import { ReactComponent as HomeIcon } from "../../assets/icons/home.svg";
import { ReactComponent as HeartIcon } from "../../assets/icons/heart.svg";
import { ReactComponent as UploadIcon } from "../../assets/icons/upload.svg";
import { ReactComponent as FileIcon } from "../../assets/icons/file.svg";
import { ReactComponent as ClockIcon } from "../../assets/icons/clock.svg";
import { ReactComponent as SettingsIcon } from "../../assets/icons/settings.svg";
import { ReactComponent as QuitIcon } from "../../assets/icons/quit.svg";
import { ReactComponent as LogoIcon } from "../../assets/icons/logo.svg";

const Navigation = () => {
  return (
    <div className="container">
      <div className="section-top">
        <a href="/" className="home">
          <LogoIcon />
        </a>
      </div>
      <div className="section-middle">
        <ul>
          <li>
            <a href="/">
              <HomeIcon />
            </a>
          </li>
          <li>
            <a href="/">
              <HeartIcon />
            </a>
          </li>
          <li>
            <a href="/">
              <UploadIcon />
            </a>
          </li>
          <li>
            <a className="active" href="/">
              <FileIcon />
            </a>
          </li>
          <li>
            <a href="/">
              <ClockIcon />
            </a>
          </li>
        </ul>
      </div>
      <div className="section-bottom">
        <ul>
          <li>
            <a href="/">
              <SettingsIcon />
            </a>
          </li>
          <li>
            <a href="/">
              <QuitIcon />
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navigation;
