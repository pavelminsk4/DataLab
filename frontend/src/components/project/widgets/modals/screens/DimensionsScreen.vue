<template>
  <section class="dimensions-list">
    <DimensionsItem
      v-for="(item, index) in dimensions"
      :key="'dimension' + index"
      :title="item.dimension.title"
      :is-disabled="!isDisabled(item.dimension.id)"
    />
  </section>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import DimensionsItem from '@/components/project/widgets/modals/screens/dimensions/DimensionsItem'

export default {
  name: 'DimensionsScreen',
  components: {DimensionsItem},
  props: {
    activeDimensions: {
      type: [Array, Object],
      default: () => [],
    },
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_SELECTED_DIMENSIONS](this.projectId)
  },
  computed: {
    ...mapGetters({
      dimensions: get.SELECTED_DIMENSIONS,
    }),
  },
  methods: {
    ...mapActions([action.GET_SELECTED_DIMENSIONS]),
    isDisabled(id) {
      return this.activeDimensions.linked_dimensions.some((el) => el === id)
    },
  },
}
</script>

<style lang="scss" scoped>
.dimensions-list {
  margin-top: 20px;

  padding: 16px 20px 40px;

  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
}
</style>
