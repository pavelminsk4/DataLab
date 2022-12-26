<template>
  <BaseModal>
    <section>
      <div class="title">Settings</div>

      <div class="settings-options">
        <div
          v-for="(item, index) in buttons"
          :key="'button' + index"
          @click="openSettings"
          :class="[
            'option',
            settingName === item.name && 'option option-active',
          ]"
        >
          {{ item.name }}
        </div>
      </div>

      <section class="form-sections">
        <div v-if="settingName === 'General'" class="settings-wrapper">
          <div class="form-title">Workspace name</div>

          <BaseInput
            v-model="title"
            :is-settings="true"
            class="input-settings"
          />

          <div class="form-title">Workspace description</div>

          <textarea
            v-model="description"
            placeholder="Description"
            class="description-field scroll"
          />
        </div>

        <div v-if="settingName === 'Permissions'" class="permissions-wrapper">
          <div class="form-title">Owner</div>
        </div>

        <BaseButton @click="saveSettings" class="button"> Save </BaseButton>
      </section>
    </section>
  </BaseModal>
</template>

<script>
import BaseModal from '@components/modals/BaseModal'
import BaseInput from '@/components/BaseInput'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'SettingsWorkspaceModal',
  components: {
    BaseButton,
    BaseInput,
    BaseModal,
  },
  data() {
    return {
      loading: false,
      title: '',
      description: '',
      settingName: 'General',
      buttons: [{name: 'General'}, {name: 'Permissions'}],
    }
  },
  props: {
    member: {
      type: [Number, String],
      default: '',
    },
    workspaceId: {
      type: Number,
      required: true,
    },
  },
  computed: {
    members() {
      let members = []
      members.push(this.member)
      return members
    },
  },
  methods: {
    openSettings(e) {
      this.settingName =
        this.settingName === e.target.innerText ? 'General' : e.target.innerText
    },
    saveSettings() {
      this.$emit('save-settings', this.title, this.description)
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 25px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
  color: var(--primary-text-color);
}

.settings-options {
  display: flex;

  border-bottom: 1px solid var(--input-border-color);

  .option {
    cursor: pointer;

    padding-bottom: 12px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
    color: rgba(255, 255, 255, 0.8);

    &:first-child {
      margin-right: 25px;
    }
  }

  .option-active {
    border-bottom: 1px solid var(--primary-button-color);

    color: var(--primary-text-color);
  }
}

.form-sections {
  display: flex;
  flex-direction: column;

  margin-top: 25px;

  .form-title {
    margin-bottom: 12px;

    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 110%;
    color: var(--primary-text-color);
  }

  .input-settings {
    margin-bottom: 24px;
  }

  .description-field {
    width: 100%;
    height: 105px;
    padding: 10px 19px;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    color: var(--primary-text-color);

    resize: none;
  }

  .description-field::placeholder {
    color: var(--secondary-text-color);
  }

  .button {
    align-self: flex-end;

    margin-top: 20px;
    width: 103px;
  }
}
</style>
