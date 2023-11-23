<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import Summary from '@components/widgets/online/SummaryWidget'
import Volume from '@components/widgets/online/VolumeWidget'
import TopSources from '@components/widgets/online/Top10BrandsWidget'
import TopCountries from '@components/widgets/online/Top10CountriesWidget'
import TopLanguages from '@components/widgets/online/Top10LanguagesWidget'
import TopAuthors from '@components/widgets/online/Top10AuthorsByVolumeWidget'
import TopSharingSources from '@components/widgets/online/TopSharingSourcesWidget'
import SentimentForPeriod from '@components/widgets/online/SentimentForPeriodWidget'
import ClippingFeedContent from '@components/widgets/online/ClippingFeedContentWidget'
import SentimentTopAuthors from '@components/widgets/online/SentimentTop10AuthorsWidget'
import SentimentTopSources from '@components/widgets/online/SentimentTop10SourcesWidget'
import SentimentTopLanguages from '@components/widgets/online/SentimentTop10LanguagesWidget'
import SentimentTopCountries from '@components/widgets/online/SentimentTop10CountriesWidget'
import ContentVolumeTopSources from '@components/widgets/online/ContentVolumeTop5SourceWidget'
import ContentVolumeTopAuthors from '@components/widgets/online/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTopCountries from '@components/widgets/online/ContentVolumeTop5CountriesWidget'
import SentimentTopKeywords from '@components/widgets/online/SentimentTopKeywordsWidget'
import TopKeywords from '@components/widgets/online/TopKeywordsWidget'
import TopKeywordsByCountry from '@components/widgets/online/TopKeywordsByCountryWidget'
import SentimentDiagram from '@components/widgets/online/SentimentDiagramWidget'
import SentimentNumberOfResults from '@components/widgets/online/SentimentNumberOfResultWidget'
import VolumeByCountry from '@components/widgets/online/VolumeByCountryWidget'
import AuthorsByCountry from '@components/widgets/online/AuthorsByCountryWidget'
import SourcesByLanguage from '@components/widgets/online/SourcesByLanguageWidget'
import SourcesByCountry from '@components/widgets/online/SourcesByCountryWidget'
import OverallTopSources from '@components/widgets/online/OverallTopSourcesWidget'
import OverallTopAuthors from '@components/widgets/online/OverallTopAuthorsWidget'
import AuthorsByLanguage from '@components/widgets/online/AuthorsByLanguageWidget'
import AuthorsBySentiment from '@components/widgets/online/AuthorsBySentimentWidget'
import LanguagesByCountry from '@components/widgets/online/LanguagesByCountryWidget'

export default {
  name: 'OnlineMainWidget',
  components: {
    ClippingFeedContent,
    Volume,
    Summary,
    TopSources,
    TopCountries,
    TopLanguages,
    TopAuthors,
    SentimentForPeriod,
    SentimentTopAuthors,
    SentimentTopSources,
    SentimentTopLanguages,
    SentimentTopCountries,
    ContentVolumeTopSources,
    ContentVolumeTopAuthors,
    ContentVolumeTopCountries,
    SentimentTopKeywords,
    TopKeywords,
    SentimentDiagram,
    SentimentNumberOfResults,
    VolumeByCountry,
    AuthorsByCountry,
    TopSharingSources,
    SourcesByLanguage,
    SourcesByCountry,
    OverallTopSources,
    OverallTopAuthors,
    AuthorsByLanguage,
    AuthorsBySentiment,
    TopKeywordsByCountry,
    LanguagesByCountry,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
