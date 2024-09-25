import { useFetchGamesList } from "../hooks/useFetchGames";

const Home = () => {
  const { gamesList, isPending } = useFetchGamesList();
  console.log("gamesList: ", gamesList);
  return (
    < div >
      <h4>hello duniyawalo! </h4>
    </div >
  )
}
export default Home;
