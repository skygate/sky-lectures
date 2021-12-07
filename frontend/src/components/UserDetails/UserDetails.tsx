import "./UserDetails.modules.scss";

import { ReactComponent as UserIcon } from "../../assets/icons/user.svg";

function UserDetails() {
  return (
    <div className="userDetails">
      <button className="userDetails--button">
        <UserIcon />
      </button>
      <p className="userDetails--name">User</p>
    </div>
  );
}

export default UserDetails;
