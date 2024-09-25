import axios from "axios";
import { API_URL } from "../constants/api";

export const gamesList = async () => {
  const res = await axios.get(`${API_URL}/games`);
  return res?.data;
};
