<template>
  <BaseModal>
    <section class="widgets-wrapper">
      <div class="title">Widgets</div>
      <BaseCheckbox
        v-for="(item, index) of widgetNames"
        :key="index"
        :label="item.default_title"
        :id="index"
        :model-value="item.is_active"
        @change="onChange"
        class="checkbox"
      >
        <span class="name">{{ item.default_title }}</span>
      </BaseCheckbox>

      <BaseButton class="button" @click="saveCollectionWidgets">
        Save
      </BaseButton>
    </section>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'WidgetsModal',
  components: {
    BaseButton,
    BaseCheckbox,
    BaseModal,
  },
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      collection: [],
    }
  },
  created() {
    this[action.GET_AVAILABLE_WIDGETS](this.projectId)
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS}),
    widgetNames() {
      if (this.widgets) {
        const availableWidgets = Object.values(this.widgets)
        return availableWidgets.filter((el) => el.default_title)
      }

      return []
    },
    collectionProxy: {
      get() {
        let collection = []
        for (let key in this.widgets) {
          if (this.widgets[key].is_active) {
            collection.push(key)
          }
        }
        return collection || []
      },
      set(val) {
        this.collection = val
      },
    },
    availableCollection() {
      const widgetsKeys = Object.keys(this.widgets)
      const notActiveWidgets = Object.assign(
        {},
        ...widgetsKeys.map((el) => ({
          [el]: {is_active: false, id: this.widgets[el].id},
        }))
      )
      const activeWidgets = Object.assign(
        {},
        ...this.collectionProxy.map((el) => ({
          [el]: {is_active: true, id: this.widgets[el].id},
        }))
      )
      return {...notActiveWidgets, ...activeWidgets}
    },
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
    removeSelectedFilter(index) {
      this.collectionProxy.splice(index, 1)
    },
    onChange(args) {
      const {id, checked} = args
      const item = Object.keys(this.widgets)[id]
      if (checked) {
        if (this.collectionProxy.indexOf(item) < 0) {
          this.collectionProxy.push(item)
        }
      } else {
        this.collectionProxy.filter((i, index) => {
          if (i === item) {
            this.removeSelectedFilter(index)
          }
        })
      }
    },
    async saveCollectionWidgets() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: this.availableCollection,
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.widgets-wrapper {
  display: flex;
  flex-direction: column;

  width: 47vw;

  .name {
    margin-left: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
  }

  .checkbox {
    margin-bottom: 10px;
  }

  .title {
    margin-bottom: 25px;

    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: 54px;
    color: var(--primary-text-color);
  }

  .button {
    align-self: flex-end;

    width: 103px;
  }
}
</style>
