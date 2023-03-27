<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :colors="colors"
    :content-volume-widget-data="genderVolume"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

const {mapActions, mapState} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialGenderVolumeWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapState(['genderVolume']),
    colors() {
      const genderColors = ['#FD7271', '#516BEE']
      const noGenderIndex = this.genderVolume.findIndex(
        (gender) => !gender.male && !gender.female
      )

      if (noGenderIndex >= 0) {
        genderColors.splice(noGenderIndex, 0, '#B0B5B8')
      }

      return genderColors
    },
  },
  created() {
    if (!this.genderVolume.length) {
      this[action.GET_GENDER_VOLUME_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_GENDER_VOLUME_WIDGET]),
  },
}
</script>
