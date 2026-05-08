.. AlaQgisPlugin documentation master file, created by
   sphinx-quickstart on Sun Feb 12 17:11:03 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:notoc:

Living Atlases QGIS Plugin
=====================================

**Date**: |today|  **Version**: |version|  

The **Living Atlases QGIS Plugin** is a downloadable plugin for `QGIS <qgis.org>`_ that gives registered users access 
to biodiversity data hosted by the ‘living atlases’.  The ‘living atlases’ are a set of organisations that share a common 
codebase, and act as nodes of the Global Biodiversity Information Facility (`GBIF <https://www.gbif.org/>`_).  These 
organisations collate and store observations of individual life forms, using the `‘Darwin Core’ <https://dwc.tdwg.org/>`_ 
data standard. galah was built and is maintained by Amanda Buyan, a member of the 
`Science & Decision Support Team <https://labs.ala.org.au/>`_ at the `Atlas of Living Australia (ALA) <https://www.ala.org.au/>`_.

The Living Atlases QGIS Plugin enables users to locate and download species occurrence records (observations, specimens, 
eDNA records, etc.), and to restrict their queries to particular taxa or locations. Users can also restrict their queries 
based on threatened and sensitive species lists, or restrict their results to occurrences that meet particular data-quality 
criteria. This data is then read into QGIS as a vector layer.

If you have any comments, questions or suggestions, please `contact us <mailto:support@ala.org.au>`_.


.. toctree::
   :maxdepth: 2

   Installation <installation>
   Getting Started <getting_started>
   User Guide <user_guide/index>
   Authors <authors>

   .. grid:: 1 2 2 2
    :gutter: 4

    .. grid-item-card::
        :link: installation.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: _static/icons/getting_started_rocket.svg
                
        **Installation**

        Want to install the Living Atlases QGIS Plugin?

    .. grid-item-card::
        :link: getting_started.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: _static/icons/configuration.svg

        **Getting Started**

        Want a quick introduction to the plugin?

    .. grid-item-card::
        :link: apidocs/galah.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: _static/icons/user_guide.svg

        **API Docs**

        Want to browse ``galah``'s API docs?
    
    .. grid-item-card:: 
        :class-card: sd-text-black
        :link: authors/index.html
        :text-align: center

        .. raw:: html
            :file: _static/icons/faq.svg

        **Authors**

        Who wrote ``galah``? Want to cite the package?