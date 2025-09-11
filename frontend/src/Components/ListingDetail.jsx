import React, { useEffect, useState, useRef, useMemo, useContext } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Axios from "axios";
import { useImmerReducer } from "use-immer";

// Contexts
import StateContext from "../Contexts/StateContext";

// Assets
import defaultBusinessMan from "./Assets/defaultBusinessman.jpg";
import defaultAgencyImage from "./Assets/defaultAgencyImage.png";

// CSS Modules
import styles from "./CSS_Modules/ListingDetail.module.css";

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
  FormControlLabel,
  Checkbox,
  IconButton,
  CardActions,
  Breadcrumbs,
  Link,
} from "@mui/material";

import LocalPhoneIcon from "@mui/icons-material/LocalPhone";
import RoomIcon from "@mui/icons-material/Room";

import ArrowCircleLeftIcon from "@mui/icons-material/ArrowCircleLeft";
import ArrowCircleRightIcon from "@mui/icons-material/ArrowCircleRight";

import moment from "moment";

const ListingDetail = () => {
  // Global state
  const navigate = useNavigate();
  const GlobalState = useContext(StateContext);

  const { id } = useParams();

  const initialState = {
    dataIsLoading: true,
    listingInfo: "",
  };

  const ReducerFunction = (draft, action) => {
    switch (action.type) {
      case "catchListingInfo":
        draft.listingInfo = action.listingObject;
        break;

      case "loadingDone":
        draft.dataIsLoading = false;
        break;

      default:
        return draft; // Return the current state if no action matches
    }
  };

  const [state, dispatch] = useImmerReducer(ReducerFunction, initialState);

  // Request to get profile info
  useEffect(() => {
    const GetListingInfo = async () => {
      try {
        const response = await Axios.get(
          `http://localhost:8000/api/listings/${id}/`
        );
        dispatch({
          type: "catchListingInfo",
          listingObject: response.data,
        });
        dispatch({ type: "loadingDone" });
      } catch (e) {
        console.log("There was a problem or the request was cancelled.");
        console.log(e.response);
      }
    };
    GetListingInfo();
  }, []);

  const listingPictures = [
    state.listingInfo.picture1,
    state.listingInfo.picture2,
    state.listingInfo.picture3,
    state.listingInfo.picture4,
    state.listingInfo.picture5,
  ].filter((picture) => picture !== null);

  const [currentPicture, setCurrentPicture] = useState(0);

  function NextPicture() {
    if (currentPicture === listingPictures.length - 1) {
      return setCurrentPicture(0);
    } else {
      return setCurrentPicture(currentPicture + 1);
    }
  }

  function PreviousPicture() {
    if (currentPicture === 0) {
      return setCurrentPicture(listingPictures.length - 1);
    } else {
      return setCurrentPicture(currentPicture - 1);
    }
  }

  if (state.dataIsLoading) {
    return (
      <Grid
        container
        justifyContent="center"
        alignItems="center"
        style={{ height: "100vh" }}
      >
        <CircularProgress />;
      </Grid>
    );
  }
  return (
    <div
      style={{ marginLeft: "2rem", marginRight: "2rem", marginBottom: "2rem" }}
    >
      <Grid item style={{ marginTop: "1rem" }}>
        <Breadcrumbs aria-label="breadcrumb">
          <Link
            underline="hover"
            color="inherit"
            onClick={() => navigate("/listings")}
            style={{ cursor: "pointer" }}
          >
            Listings
          </Link>
          <Typography sx={{ color: "text.primary" }}>
            {state.listingInfo.title}
          </Typography>
        </Breadcrumbs>
      </Grid>

      {/* Image slider */}
      {listingPictures.length > 0 ? (
        <Grid
          item
          container
          justifyContent="center"
          className={styles.sliderContainer}
        >
          {listingPictures.map((picture, index) => {
            return (
              <div key={index}>
                {index === currentPicture ? (
                  <img src={picture} className={styles.picture} />
                ) : (
                  ""
                )}
              </div>
            );
          })}

          <ArrowCircleLeftIcon
            onClick={PreviousPicture}
            className={styles.sliderArrowLeft}
          />
          <ArrowCircleRightIcon
            onClick={NextPicture}
            className={styles.sliderArrowRight}
          />
        </Grid>
      ) : (
        ""
      )}

      {/* More information about the listing */}

      <Grid item container>
        <Grid item container xs={7} direction="column">
          <Grid item>
            <Typography variant="h5"> {state.listingInfo.title} </Typography>
          </Grid>
          <Grid item>
            <RoomIcon fontSize="small" />{" "}
            <Typography variant="h6"> {state.listingInfo.borough} borough </Typography>
          </Grid>
          <Grid item>
            <Typography>
              Posted on{" "}
              {moment(state.listingInfo.date_posted).format(
                "MMMM Do YYYY, h:mm a"
              )}
            </Typography>
          </Grid>
        </Grid>
        <Grid item container xs={5} alignItems='center'>
          <Typography>
            {" "}
            {state.listingInfo.listing_type} | {state.listingInfo.price}{" "}
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default ListingDetail;
