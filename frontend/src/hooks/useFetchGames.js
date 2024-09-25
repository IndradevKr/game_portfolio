import { useQuery } from "@tanstack/react-query"
import { gamesList } from "../api/games.api"

export const useFetchGamesList = () => {
  const { data, isFetching, isPending, error } = useQuery({
    queryKey: ['games-list'],
    queryFn: async () => await gamesList(),
  })
  return {
    gamesList: data,
    isFetching,
    isPending,
    error
  }
}
