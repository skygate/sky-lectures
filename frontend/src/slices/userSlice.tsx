import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
const API_URL = "http://localhost:8000/api/";
export const logIn = createAsyncThunk(
  "user/login",
  async (username, password) => {
    return axios
      .post(
        API_URL +
          {
            username,
            password,
          }
      )
      .then((response) => {
        console.log(response);
      });
  }
);
export const userSlice = createSlice({
  name: "user",
  initialState: {
    user: null,
  },
  reducers: {},
  extraReducers: {
    //@ts-ignore
    [logIn.pending]: (state) => {
      state.status = "loading";
    },
    //@ts-ignore
    [logIn.fulfilled]: (state, action) => {
      state.status = "loading";
      state.user = action.payload;
    },
    //@ts-ignore
    [logIn.rejected]: (state) => {
      state.status = "failed";
    },
  },
});

export default userSlice.reducer;
