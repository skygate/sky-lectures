import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import type { RootState } from "../store/store";

interface UserCredentials {
  email: string;
  password: string;
}

interface AuthError {
  message: string;
}

interface AuthState {
  isAuth: boolean;
  isLoading: boolean;
  currentUser?: CurrentUser;
  error?: AuthError;
}

interface CurrentUser {
  id: string;
}

const initialState: AuthState = {
  isAuth: false,
  isLoading: false,
};

export const register = createAsyncThunk(
  "auth/register",
  async ({ email, password }: UserCredentials) => {
    try {
      // const response = await
      console.log("async call", email, password);
    } catch (error) {
      console.log(error);
    }
  }
);

export const login = createAsyncThunk(
  "auth/login",
  async ({ email, password }: UserCredentials) => {
    try {
      // const response = await
      console.log("async", email, password);
    } catch (error) {
      console.log("error");
    }
  }
);

export const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    setLoading: (state) => {
      state.isLoading = true;
    },
    setAuthSuccess: (state, { payload }) => {
      state.isAuth = true;
      state.isLoading = false;
      state.currentUser = payload;
    },
    setLogOut: (state) => {
      state.isAuth = false;
      state.isLoading = false;
      state.currentUser = undefined;
    },
    setAuthFailed: (state, { payload }) => {
      state.isAuth = false;
      state.isLoading = false;
      state.error = payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(register.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.isLoading = false;
        // state.currentUser = action.payload;
      })
      .addCase(register.rejected, (state) => {
        state.isLoading = false;
        state.isAuth = false;
      })
      .addCase(login.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(login.fulfilled, (state) => {
        state.isAuth = true;
        state.isLoading = false;
        // state.currentUser = action.payload;
      })
      .addCase(login.rejected, (state) => {
        state.isAuth = false;
        state.isLoading = false;
      });
  },
});

export const { setLoading, setAuthSuccess, setLogOut, setAuthFailed } =
  authSlice.actions;

export const authSelector = (state: RootState) => state.auth;

export default authSlice.reducer;
