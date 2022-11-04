<template>
  <div v-if="currentProject">
    <WidgetsModal
      v-if="isOpenWidgetsModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenWidgetsModal')"
    />

    <AllDimensionsModal
      v-if="isOpenDimensionModal"
      @close="toggleWidgetsModal('isOpenDimensionModal')"
    />

    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      :hint="'Search by keywords and phrases '"
    />

    <div class="navigation-bar">
      <div
        class="dimensions-button"
        @click="toggleWidgetsModal('isOpenDimensionModal')"
      >
        <DimensionsIcon />
      </div>

      <BaseButton
        class="button"
        @click="toggleWidgetsModal('isOpenWidgetsModal')"
      >
        <PlusIcon class="icon" />
        Add Widgets
      </BaseButton>
    </div>
    <WidgetsView :project-id="currentProject.id" />
  </div>
</template>

<script>
import NavigationBar from '@/components/navigation/NavigationBar'
import WidgetsView from '@/components/widgets/WidgetsView'
import BaseButton from '@/components/buttons/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'
import WidgetsModal from '@/components/modals/WidgetsModal'
import DimensionsIcon from '@/components/icons/DimensionsIcon'
import AllDimensionsModal from '@/components/widgets/modals/AllDimensionsModal'

export default {
  name: 'AnalyticsScreen',
  components: {
    AllDimensionsModal,
    DimensionsIcon,
    WidgetsModal,
    PlusIcon,
    BaseButton,
    WidgetsView,
    NavigationBar,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      isOpenWidgetsModal: false,
      isOpenDimensionModal: false,
    }
  },
  methods: {
    toggleWidgetsModal(val) {
      this[val] = !this[val]
    },
  },
}
</script>

<style lang="scss" scoped>
.navigation-bar {
  display: flex;
  justify-content: flex-end;

  margin-top: 30px;

  .button {
    width: 155px;

    .icon {
      margin-right: 10px;
    }
  }
}

.dimensions-button {
  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;

  margin-right: 10px;
  width: 40px;
  height: 40px;

  background: #29303d;
  border-radius: 8px;
}
</style>
