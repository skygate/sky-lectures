import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import App from "./App";
import Page from "./components/Page/Page";
import Player from "./screens/Player/Player";
import { store } from "./store/store";
import SignUp from "./screens/SignUp/SingUp";
import SignIn from "./screens/SignIn/SignIn";
import Favorites from "./screens/Favorites/Favorites";
import History from "./screens/History/History";
import Schedule from "./screens/Schedule/Schedule";
import reportWebVitals from "./reportWebVitals";

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <Page>
                <App />
              </Page>
            }
          />
          <Route path="/SignIn" element={<SignIn />} />
          <Route path="/SignUp" element={<SignUp />} />
          <Route
            path="/player"
            element={
              <Page>
                <Player />
              </Page>
            }
          />
          <Route
            path="/favorites"
            element={
              <Page>
                <Favorites />
              </Page>
            }
          />
          <Route
            path="/history"
            element={
              <Page>
                <History />
              </Page>
            }
          />
          <Route
            path="/schedule"
            element={
              <Page>
                <Schedule />
              </Page>
            }
          />
        </Routes>
      </BrowserRouter>
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
