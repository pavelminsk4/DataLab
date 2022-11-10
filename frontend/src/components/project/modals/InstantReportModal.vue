<template>
  <BaseModal modal-frame-style="width: auto; height: 45vh;">
    <div class="title">Template settings</div>

    <div class="wrapper-buttons">
      <BaseSelect
        v-model="template"
        placeholder="Select Template"
        name="template"
        :list="titleTemplates"
        :is-reject-selection="false"
        @select-option="selectItem"
        class="select"
      />

      <BaseButton
        :is-not-background="true"
        @click="saveTemplate"
        class="button"
      >
        Save Template
      </BaseButton>

      <a class="link" :href="`/projects/${projectId}/reports/instantly_report`">
        Download
      </a>
    </div>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/buttons/BaseButton'
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import BaseSelect from '@/components/BaseSelect'

export default {
  name: 'InstantReportModal',
  components: {BaseSelect, BaseButton, BaseModal},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
  },
  data() {
    return {
      template: '',
    }
  },
  created() {
    this[action.GET_TEMPLATES]()
  },
  computed: {
    ...mapGetters({
      templates: get.TEMPLATES,
    }),
    titleTemplates() {
      return this.templates.map((el) => el.title)
    },
  },
  methods: {
    ...mapActions([action.GET_TEMPLATES, action.UPDATE_PROJECT]),
    selectItem(name, val) {
      let element = this.templates.filter((el) => el.title === val)
      this.template = element[0]
    },
    saveTemplate() {
      this[action.UPDATE_PROJECT]({
        projectId: this.projectId,
        data: {
          report_template: this.template.id,
        },
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 40px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}

.wrapper-buttons {
  display: flex;
  gap: 14px;

  .select {
    width: 408px;
  }

  .button {
    width: 160px;
  }

  .link {
    display: flex;

    text-decoration: none;

    width: 128px;
    padding: 10px 30px;

    background: var(--primary-button-color);
    border-radius: 8px;

    color: var(--primary-text-color);

    font-style: normal;
    font-weight: 600;
    font-size: 14px;
    line-height: 20px;

    &:hover {
      background: rgba(5, 95, 252, 0.6);
    }
  }
}
</style>
