<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import SummaryWidget from '@/components/widgets/online/SummaryWidget'
import VolumeWidget from '@/components/widgets/online/VolumeWidget'
import Top10BrandsWidget from '@/components/widgets/online/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/widgets/online/Top10CountriesWidget'
import Top10LanguagesWidget from '@/components/widgets/online/Top10LanguagesWidget'
import Top10AuthorsByVolumeWidget from '@/components/widgets/online/Top10AuthorsByVolumeWidget'
import TopSharingSources from '@/components/widgets/online/TopSharingSourcesWidget'
import SentimentForPeriodWidget from '@/components/widgets/online/SentimentForPeriodWidget'
import ClippingFeedContentWidget from '@/components/widgets/online/ClippingFeedContentWidget'
import SentimentTop10AuthorsWidget from '@/components/widgets/online/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/widgets/online/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/widgets/online/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/widgets/online/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/widgets/online/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/widgets/online/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/widgets/online/ContentVolumeTop5CountriesWidget'
import SentimentTopKeywords from '@/components/widgets/online/SentimentTopKeywordsWidget'
import TopKeywords from '@/components/widgets/online/TopKeywordsWidget'
import SentimentDiagram from '@/components/widgets/online/SentimentDiagramWidget'
import SentimentNumberOfResults from '@/components/widgets/online/SentimentNumberOfResultWidget'
import AuthorsByCountry from '@/components/widgets/online/AuthorsByCountryWidget'

export default {
  name: 'OnlineMainWidget',
  components: {
    ClippingFeedContentWidget,
    VolumeWidget,
    SummaryWidget,
    Top10BrandsWidget,
    Top10CountriesWidget,
    Top10LanguagesWidget,
    SentimentForPeriodWidget,
    Top10AuthorsByVolumeWidget,
    SentimentTop10AuthorsWidget,
    SentimentTop10SourcesWidget,
    SentimentTop10LanguagesWidget,
    SentimentTop10CountriesWidget,
    ContentVolumeTop5SourceWidget,
    ContentVolumeTop5AuthorsWidget,
    ContentVolumeTop5CountriesWidget,
    SentimentTopKeywords,
    TopKeywords,
    SentimentDiagram,
    SentimentNumberOfResults,
    AuthorsByCountry,
    TopSharingSources,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
