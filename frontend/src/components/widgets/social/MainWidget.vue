<template>
  <component
    :is="widgetDetails.widgetName"
    v-bind="$attrs"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import SummaryWidget from '@/components/widgets/social/SummaryWidget'
import ClippingFeedContentWidget from '@/components/widgets/social/ClippingFeedContentWidget'
import ContentVolumeWidget from '@/components/widgets/social/ContentVolumeWidget'
import TopLocationsWidget from '@/components/widgets/social/TopLocationsWidget'
import TopLanguagesWidget from '@/components/widgets/social/TopLanguagesWidget'
import TopAuthorsWidget from '@/components/widgets/social/TopAuthorsWidget'
import ContentVolumeByTopLocationsWidget from '@/components/widgets/social/ContentVolumeTopLocationsWidget'
import ContentVolumeByTopAuthorsWidget from '@/components/widgets/social/ContentVolumeTopAuthorsWidget'
import ContentVolumeByTopLanguagesWidget from '@/components/widgets/social/ContentVolumeTopLanguagesWidget'

export default {
  name: 'SocialMainWidget',
  components: {
    ClippingFeedContentWidget,
    SummaryWidget,
    ContentVolumeWidget,
    TopLocationsWidget,
    TopLanguagesWidget,
    TopAuthorsWidget,
    ContentVolumeByTopLocationsWidget,
    ContentVolumeByTopAuthorsWidget,
    ContentVolumeByTopLanguagesWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
}
</script>
