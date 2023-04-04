<template>
  <FeaturesScreen
    :number-of-posts="numberOfPosts"
    :current-project="currentProject"
  />
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import FeaturesScreen from '@/components/project/screens/FeaturesScreen'

export default {
  name: 'SocialFeaturesView',
  components: {FeaturesScreen},
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  computed: {
    ...mapGetters({
      numberOfPosts: get.POSTS_NUMBER,
    }),
  },
}
</script>
