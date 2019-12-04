## Build Conda Environment
`conda create -n thisiship --file requirements.txt -c conda-forge`
`conda activate`

## scrape events from facebook
`python scrape.py`

## generate index from scraped events
`python generator.py`