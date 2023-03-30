<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="sharing-sources-wrapper">
      <SharingSourcesWidget
        v-for="(item, index) in topSharingSources"
        :key="'source' + index"
        :type="item.type"
        :img="item.picture"
        :name="item.name"
        :alias="item.alias"
        :value="item.value"
        :widget-details="widgetDetails"
      >
        <template #chips>
          <div class="type">
            <component :is="capitalizeFirstLetter(item.source) + 'Icon'" />
            {{ item.source }}
          </div>
          <div :class="['type', item.gender]">
            <component :is="capitalizeFirstLetter(item.gender) + 'Icon'" />
            {{ item.gender }}
          </div>
        </template>
      </SharingSourcesWidget>
    </div>
  </component>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {capitalizeFirstLetter} from '@/lib/utilities'

import MaleIcon from '@/components/icons/MaleIcon'
import FemaleIcon from '@/components/icons/FemaleIcon'
import TwitterIcon from '@/components/icons/TwitterIcon'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import SharingSourcesWidget from '@/components/widgets/SharingSourcesWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'TopSharingSourcesWidget',
  components: {
    WidgetsLayout,
    SharingSourcesWidget,
    MaleIcon,
    FemaleIcon,
    TwitterIcon,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topSharingSources() {
      return this.socialWidgets.topSharingSources
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    if (!this.topSharingSources.length) {
      this[action.GET_TOP_SHARING_SOURCES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_SHARING_SOURCES]),
    capitalizeFirstLetter,
  },
}
</script>

<style scoped>
.sharing-sources-wrapper {
  display: flex;
  gap: 12px;
}

.type {
  display: flex;
  gap: 4px;

  padding: 6px 8px;

  background: var(--chips-background-secondary-color);
  border-radius: 2px 12px 12px 2px;

  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 16px;
  color: var(--typography-primary-color);
}

.male {
  background-color: var(--male-bg-color);
}

.female {
  background-color: var(--female-bg-color);
}
</style>
