import Sidebar from "./components/Sidebar/Sidebar";
import Searchbar from "./components/Searchbar/Searchbar";
import Header from "./components/Header/Header";
import UserDetails from "./components/UserDetails/UserDetails";

import "./App.modules.scss";

function App() {
  return (
    <div className="App">
      <Sidebar />
      <div className="App__container">
        <Header>
          <Searchbar />
          <UserDetails />
        </Header>
      </div>
    </div>
  );
}

export default App;
