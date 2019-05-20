cat input.csv | parallel --header : --pipe -N 10 'cat > output{#}.csv'
