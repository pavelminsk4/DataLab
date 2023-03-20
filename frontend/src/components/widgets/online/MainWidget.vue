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
import SentimentForPeriodWidget from '@/components/widgets/online/SentimentForPeriodWidget'
import ClippingFeedContentWidget from '@/components/widgets/online/ClippingFeedContentWidget'
import SentimentTop10AuthorsWidget from '@/components/widgets/online/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/widgets/online/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/widgets/online/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/widgets/online/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/widgets/online/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/widgets/online/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/widgets/online/ContentVolumeTop5CountriesWidget'

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
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
