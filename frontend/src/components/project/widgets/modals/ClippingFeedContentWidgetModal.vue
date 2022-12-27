<template>
  <BaseModal modal-frame-style="width: 50vw;">
    <div class="main-title">{{ clippingFeedContent.title }}</div>

    <div class="settings-wrapper">
      <div class="options-wrapper">
        <div class="title-general">General</div>

        <div class="title">Widget Title</div>
        <BaseInput v-model="title" class="input-title" />

        <div class="title">Widget Description</div>
        <textarea
          class="description-field scroll"
          placeholder="Some words about Widgets"
          v-model="description"
        />

        <BaseButton @click="saveOptions">Save</BaseButton>
      </div>
    </div>
  </BaseModal>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseInput from '@/components/BaseInput'
import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'ClippingFeedContentWidgetModal',
  components: {BaseButton, BaseInput, BaseModal},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      title: '',
      description: '',
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS}),
    clippingFeedContent() {
      return this.widgets['clipping_feed_content_widget']
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_AVAILABLE_WIDGETS,
    ]),
    async saveOptions() {
      await this[action.UPDATE_AVAILABLE_WIDGETS]({
        projectId: this.projectId,
        data: {
          clipping_feed_content_widget: {
            id: this.clippingFeedContent.id,
            title: this.title || this.clippingFeedContent.title,
            description:
              this.description || this.clippingFeedContent.description,
          },
        },
      })
      await this[action.GET_AVAILABLE_WIDGETS](this.projectId)
      await this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.main-title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.input-title {
  width: 100%;
}

.description-field {
  width: 100%;
  height: 132px;
  padding: 12px 16px;
  margin-bottom: 25px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  resize: none;
}

.description-field::placeholder {
  color: var(--secondary-text-color);
}

.settings-wrapper {
  display: flex;

  min-width: 100%;
  .options-wrapper {
    display: flex;
    flex-direction: column;

    width: 100%;

    .title-general {
      padding-bottom: 10px;
      margin-bottom: 15px;

      border-bottom: 1px solid var(--primary-button-color);

      font-weight: 400;
      font-size: 14px;
      line-height: 22px;
    }

    .title {
      margin: 25px 0 12px;

      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 110%;
    }

    .option {
      margin-bottom: 25px;
    }
  }
}
</style>
