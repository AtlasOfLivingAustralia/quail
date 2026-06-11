# Quail (EXPERIMENTAL)

<!-- # Quail <a href="https://galah.ala.org.au/Python/"><img src="docs/source/_static/logo/logo.png" align="right" style="margin: 0px 10px 0px 10px;" alt="" height="138"/></a> -->

<!-- badges: start -->

[![Codecov test coverage](https://codecov.io/gh/AtlasOfLivingAustralia/galah-python/branch/main/graph/badge.svg)](https://app.codecov.io/gh/AtlasOfLivingAustralia/galah-python?branch=main)

<!-- badges: end -->

## Overview

`Quail` is a plugin for [QGIS](https://qgis.org/) designed for users to 
interface with biodiversity data in the [Atlas of Living Australia](https://www.ala.org.au) 
(ALA).  The ALA organises, collates and stores observations of individual life forms, 
using the [‘Darwin Core’](https://dwc.tdwg.org/) data standard.  `Quail` 
was built and is maintained by the [Science & Decision Support Team](https://labs.ala.org.au) 
at the ALA.

`Quail` enables users to locate and download species occurrence records
(observations, specimens, eDNA records, etc.), taxonomic information, or
associated media such as images or sounds, and to restrict their queries
to particular taxa or locations. Users can either download a species list or a 
set of occurrence records.

If you have any comments, questions or suggestions, please [contact
us](mailto:support@ala.org.au).

## Installation (QGIS)

When you load QGIS, go to `Plugins`->`Manage and Install Plugins`.  Under the 
`Not installed` option, search for `Quail` and install it.  You are 
then ready to go!

## Getting started

The `Getting Started Tutorial` provides an introduction on how to use the plugin.

## Usage

View the `Quail website` for documentations and vignettes to get started.

## Licence 
This plugin was created and designed by Amanda Buyan under a MPL-2.0 licence, with 
additional support and help from the Science and Decision Support Team, Kylie Morrow, 
Tania Laity, Juliet Seers and Cameron Slatyer.

-----------------------------------------------------

## For developers of the ALA QGIS Package

#### Homebrew/Chocolately

A lot of the programs required for development and contribution need to be installed 
on your computer, NOT through the Python Package Index, but by an external source.  
For Macs/Linux, I recommend [homebrew](https://brew.sh/).  For Windows, I have seen 
[Chocolatey](https://chocolatey.org/), though have not tried it myself.

All of the required packages for Homebrew/Chocolately are in ```brew.txt```.  

Homebrew:

```
<brew.txt xargs brew install
```

#### PyPI

I have put all the required Python packages for development in a ```requirements.txt``` 
folder.  Run

```
pip install -r requirements.txt
```