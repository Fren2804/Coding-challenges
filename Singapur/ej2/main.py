def getMaxRequests(bandwidth, request, totalBandwidth):
    dp = [0] * (totalBandwidth + 1)

    for coste, solicitudes in zip(bandwidth, request):
        print(dp)
        print("cost: ", coste, " sol: ", solicitudes)
        for disponible in range(totalBandwidth, coste - 1, -1):
            print(disponible, coste)
            dp[disponible] = max(
                dp[disponible],                      
                dp[disponible - coste] + solicitudes
            )
    print(len(dp))
    print(dp)

    return dp[totalBandwidth]

if __name__ == "__main__":
    totalBandwidth = 50

    bandwidth = [10, 20, 30, 15, 5]
    request   = [60, 100, 120, 70, 30]

    resultado = getMaxRequests(bandwidth, request, totalBandwidth)

    print("Resultado:", resultado)
    print("Esperado: ", 763)