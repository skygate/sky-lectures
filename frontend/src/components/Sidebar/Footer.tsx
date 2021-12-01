import { ReactComponent as SettingsIcon } from "../../assets/icons/settings.svg";
import { ReactComponent as QuitIcon } from "../../assets/icons/quit.svg";

import "./Footer.modules.scss";

function Footer() {
  return (
    <div className="sidebar__footer">
      <ul>
        <li>
          <button>
            <SettingsIcon />
          </button>
        </li>
        <li>
          <button>
            <QuitIcon />
          </button>
        </li>
      </ul>
    </div>
  );
}

export default Footer;
