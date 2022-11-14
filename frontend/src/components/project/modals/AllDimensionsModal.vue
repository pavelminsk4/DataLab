<template>
  <BaseModal modal-frame-style="width: 40vw; height: 80vh;">
    <div class="title">Widgets Dimensions</div>
    <div class="dimensions-wrapper">
      <div
        v-for="(item, index) in dimensions"
        :key="'dimension' + index"
        class="dimension"
      >
        <div>{{ item.title }}</div>
        <BaseCheckbox :id="item.id" @change="onChange" />
      </div>
    </div>

    <BaseButton class="button"> Save </BaseButton>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'AllDimensionsModal',
  components: {BaseButton, BaseCheckbox, BaseModal},
  data() {
    return {
      collectionProxy: [],
    }
  },
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
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.collectionProxy.push(args)
      } else {
        let element = this.collectionProxy.indexOf(id)
        this.removeSelectedFilter(element, id)
      }

      console.log(this.collectionProxy)
    },
    removeSelectedFilter(index) {
      this.collectionProxy.splice(index, 1)
    },
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
  display: flex;
  justify-content: space-between;

  cursor: pointer;

  padding-bottom: 16px;
  margin-bottom: 16px;

  border-bottom: 1px solid #2d2d31;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.button {
  width: 100%;
  margin-top: 22px;
}
</style>
