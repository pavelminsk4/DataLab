<template>
  <BaseModal modal-frame-style="width: 40vw; height: 80vh;">
    <div class="title">Widgets Dimensions</div>
    <div class="dimensions-wrapper">
      <div
        v-for="(item, index) in dimensions"
        :key="'d' + index"
        class="dimension"
      >
        {{ item.title }}
      </div>
    </div>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

export default {
  name: 'AllDimensionsModal',
  components: {BaseModal},
  computed: {
    ...mapGetters({
      dimensions: get.DIMENSIONS,
    }),
  },
  created() {
    this[action.GET_DIMENSIONS]()
  },
  methods: {
    ...mapActions([action.GET_DIMENSIONS]),
  },
}
</script>

<style scoped>
.title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.dimensions-wrapper {
  padding: 37px 46px 31px 33px;

  background: #242529;
  border: 1px solid #2d2d31;
  box-shadow: 0px 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
}

.dimension {
  cursor: pointer;

  padding-bottom: 16px;
  margin-bottom: 16px;

  border-bottom: 1px solid #2d2d31;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}
</style>
