import React, { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import Axios from "axios";
import { useImmerReducer } from "use-immer";

// MUI imports
import {
  Grid,
  AppBar,
  Typography,
  Button,
  Card,
  CardHeader,
  CardMedia,
  CardContent,
  CircularProgress,
  TextField,
  Snackbar,
} from "@mui/material";

// Custom imports
import styles from "./CSS_Modules/Register.module.css";

const data = {
  username: "testinguser",
  email: "t@lbrep.com",
  password: "mypass123",
  re_password: "mypass123",
};

function Register() {
  const navigate = useNavigate();
  const URL = "http://localhost:8000/api-auth-djoser/users/";

  const initialState = {
    usernameValue: "",
    emailValue: "",
    passwordValue: "",
    password2Value: "",
    sendRequest: 0,
    openSnack: false,
    disableBtn: false,
  };

  const ReducerFunction = (draft, action) => {
    switch (action.type) {
      case "catchUsernameChange":
        draft.usernameValue = action.usernameChosen;
        break;
      case "catchEmailChange":
        draft.emailValue = action.emailChosen;
        break;
      case "catchPasswordChange":
        draft.passwordValue = action.passwordChosen;
        break;
      case "catchPassword2Change":
        draft.password2Value = action.password2Chosen;
        break;
      case "changeSendRequest":
        draft.sendRequest += 1;
        break;
      case "openTheSnack":
        draft.openSnack = true;
        break;
      case "disableTheButton":
        draft.disableBtn = true;
        break;
      case "allowTheButton":
        draft.disableBtn = false;
        break;

      default:
        return draft; // Return the current state if no action matches
    }
  };

  const [state, dispatch] = useImmerReducer(ReducerFunction, initialState);

  const FormSubmit = (e) => {
    e.preventDefault();
    data.username = state.usernameValue;
    data.email = state.emailValue;
    data.password = state.passwordValue;
    data.re_password = state.password2Value;
    // setSendRequest((prev) => !prev);
    dispatch({ type: "changeSendRequest" });
    dispatch({ type: "disableTheButton" });
  };

  useEffect(() => {
    if (state.sendRequest) {
      const source = Axios.CancelToken.source();
      const SignUp = async () => {
        try {
          const response = await Axios.post(URL, data, {
            cancelToken: source.token,
          });
          console.log("User registered successfully:", response);
          dispatch({ type: "openTheSnack" });
        } catch (error) {
          console.error("Error registering user:", error, error.response.data);
          dispatch({ type: "allowTheButton" });
        }
      };
      SignUp();
      return () => {
        source.cancel("Component unmounted, request cancelled");
      };
    }
  }, [state.sendRequest]);

  useEffect(() => {
    if (state.openSnack) {
      const timer = setTimeout(() => {
        navigate("/");
      }, 1500);
      return () => clearTimeout(timer);
    }
  }, [state.openSnack]);

  return (
    <div className={styles.formContainer}>
      <form onSubmit={FormSubmit}>
        <Grid item container justifyContent="center">
          <Typography variant="h4">CREATE AN ACCOUNT</Typography>
        </Grid>
        <Grid item container className={styles.formItem}>
          <TextField
            id="username"
            label="Username"
            variant="outlined"
            fullWidth
            value={state.usernameValue}
            onChange={(e) =>
              dispatch({
                type: "catchUsernameChange",
                usernameChosen: e.target.value,
              })
            }
          />
        </Grid>
        <Grid item container className={styles.formItem}>
          <TextField
            id="email"
            label="Email"
            variant="outlined"
            fullWidth
            type="email"
            value={state.emailValue}
            onChange={(e) =>
              dispatch({
                type: "catchEmailChange",
                emailChosen: e.target.value,
              })
            }
          />
        </Grid>
        <Grid item container className={styles.formItem}>
          <TextField
            id="password"
            label="Password"
            variant="outlined"
            fullWidth
            type="password"
            value={state.passwordValue}
            onChange={(e) =>
              dispatch({
                type: "catchPasswordChange",
                passwordChosen: e.target.value,
              })
            }
          />
        </Grid>
        <Grid item container className={styles.formItem}>
          <TextField
            id="password2"
            label="Confirm Password"
            variant="outlined"
            fullWidth
            type="password"
            value={state.password2Value}
            onChange={(e) =>
              dispatch({
                type: "catchPassword2Change",
                password2Chosen: e.target.value,
              })
            }
          />
        </Grid>
        <Grid item container className={styles.registerDiv} xs={8}>
          <Button
            className={styles.registerBtn}
            variant="contained"
            color="primary"
            type="submit"
            fullWidth
            disabled={state.disableBtn}
          >
            SIGN UP
          </Button>
        </Grid>
      </form>
      <Grid
        item
        container
        justifyContent="center"
        className={styles.loginPrompt}
      >
        <Typography variant="small">
          Already have an account?{" "}
          <span
            className={styles.signinLink}
            onClick={() => navigate("/login")}
          >
            SIGN IN
          </span>
        </Typography>
      </Grid>
            <Snackbar
              open={state.openSnack}
              message="You have successfully created an account!"
              anchorOrigin={{ vertical: "bottom", horizontal: "center" }}
              // className={styles.snackbar}
              // autoHideDuration={3000}
              // ContentProps={{ style: { backgroundColor: "blue", color: "white" } }}
              ContentProps={{class: styles.snackbar}}
            />

    </div>
  );
}

export default Register;
