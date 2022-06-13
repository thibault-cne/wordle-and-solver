package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/opts"
	"github.com/go-echarts/go-echarts/v2/types"
)

func main() {
	line := createLineChart()

	f, err := os.Create("./Data/line.html")

	if err != nil {
		panic(err)
	}

	defer f.Close()

	line.Render(f)
}

func createLineChart() *charts.Line {
	line := charts.NewLine()

	line.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{
			Title: "Temps de calcul moyen en fonction de la taille du mot",
		}),
		charts.WithInitializationOpts(opts.Initialization{
			Theme: types.ThemeInfographic,
		}),
	)

	line.SetXAxis([]string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}).
		AddSeries("Serie A", generateData()).
		SetSeriesOptions(
			charts.WithLineChartOpts(opts.LineChart{
				Smooth: true,
			}),
		)

	return line
}

func generateData() []opts.LineData {
	items := make([]opts.LineData, 0)
	for i := 1; i < 10; i++ {
		err := os.Remove("./Data/wsolf.txt")

		if err != nil {
			panic(err)
		}

		f, err := os.Create("./Data/wsolf.txt")

		if err != nil {
			panic(err)
		}

		defer f.Close()

		_, err2 := f.WriteString(fmt.Sprintf("%d", i))

		if err2 != nil {
			panic(err2)
		}

		items = append(items, opts.LineData{
			Value: getExecutionTime(),
		})
		fmt.Println(i)
	}

	return items
}

func getExecutionTime() float64 {
	start := time.Now()

	cmd := exec.Command("./Test")

	if err := cmd.Run(); err != nil {
		panic(err)
	}

	return time.Since(start).Seconds()
}
